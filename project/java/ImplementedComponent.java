package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  The set of components that are implemented in a given system inventory item.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImplementedComponent  {

  private String component-uuid;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;

}