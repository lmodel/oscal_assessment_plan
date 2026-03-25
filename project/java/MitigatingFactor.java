package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Describes an existing mitigating factor that may affect the overall determination of the risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MitigatingFactor  {

  private String uuid;
  private String description;
  private String implementation-uuid;
  private List<SubjectReference> subjects;
  private List<Property> props;
  private List<Link> links;

}