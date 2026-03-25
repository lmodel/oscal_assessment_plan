package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Used to select a control objective for inclusion/exclusion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SelectObjectiveById  {

  private String objective-id;
  private String remarks;

}